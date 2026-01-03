import numpy as np
import scipy.signal as signal

# =================================================================
# PROJECT PHOENIX: REFERENCE IMPLEMENTATION
# Physical Layer: Fractal Recursive Baseband Modulation (FRBM)
# employing Generalized Frequency Division Multiplexing (GFDM)
# =================================================================

class FractalBasebandModulator:
    def __init__(self, sample_rate=512000):
        self.fs = sample_rate
        
        # DEFINITION OF FRACTAL NODES (Level 1 Hierarchy)
        # Node 0: Sonic (Robust Core)
        # Node 1: Supersonic (Data Payload)
        self.nodes = {
            'sonic':      {'offset': 0,      'qam': 64,   'filter_alpha': 0.3},
            'supersonic': {'offset': 60000,  'qam': 1024, 'filter_alpha': 0.1}
        }

    def generate_constellation(self, bits, order):
        """Maps bits to Complex QAM Constellation (The 'Data Leaf')."""
        num_symbols = len(bits) // int(np.log2(order))
        # Simplified mapping for simulation
        return (np.random.randint(0, int(np.sqrt(order)), num_symbols) * 2 - 1) + \
               1j * (np.random.randint(0, int(np.sqrt(order)), num_symbols) * 2 - 1)

    def gfdm_kernel(self, symbols, subcarriers, subsymbols, alpha):
        """
        The GFDM Modulation Kernel.
        Applies per-subcarrier pulse shaping (RRC) to minimize spectral bleed.
        """
        total_len = subcarriers * subsymbols
        signal_out = np.zeros(total_len, dtype=complex)
        
        # Prototype Filter (Root Raised Cosine approximation)
        # In FRBM, Alpha is tuned per Node for optimal spectral containment
        t = np.linspace(-1, 1, total_len)
        g = np.sinc(t) * np.cos(np.pi * alpha * t) / (1 - (2 * alpha * t)**2)

        for k in range(subcarriers):
            for m in range(subsymbols):
                idx = k * subsymbols + m
                if idx < len(symbols):
                    # Circular Convolution in Frequency Domain
                    subcarrier = symbols[idx] * np.roll(g, m*subcarriers)
                    # Mix to subcarrier frequency
                    mix = subcarrier * np.exp(1j * 2 * np.pi * k * np.arange(total_len) / subcarriers)
                    signal_out += mix
        return signal_out

    def synthesize_fractal(self, bits_sonic, bits_supersonic):
        """
        THE FRACTAL SYNTHESIZER
        Recursively modulates nodes and sums them into the Master Baseband.
        """
        # 1. Synthesize Node A (Sonic)
        print(f"Synthesizing Fractal Node A (Sonic)...")
        sym_sonic = self.generate_constellation(bits_sonic, self.nodes['sonic']['qam'])
        # Sonic node uses fewer subcarriers for robustness
        sig_sonic = self.gfdm_kernel(sym_sonic, subcarriers=16, subsymbols=8, 
                                   alpha=self.nodes['sonic']['filter_alpha'])

        # 2. Synthesize Node B (Supersonic)
        print(f"Synthesizing Fractal Node B (Supersonic)...")
        sym_super = self.generate_constellation(bits_supersonic, self.nodes['supersonic']['qam'])
        # Supersonic node uses high density subcarriers
        sig_super = self.gfdm_kernel(sym_super, subcarriers=64, subsymbols=8, 
                                   alpha=self.nodes['supersonic']['filter_alpha'])

        # 3. Recursive Summation
        # Ensure lengths align
        min_len = min(len(sig_sonic), len(sig_super))
        t = np.arange(min_len)
        
        # Mix Node A to Baseband (0 Hz relative)
        final_sonic = sig_sonic[:min_len] 
        
        # Mix Node B to Frequency Offset
        # This placement relies on the sharp filtering of the GFDM kernel
        final_super = sig_super[:min_len] * np.exp(1j * 2 * np.pi * self.nodes['supersonic']['offset'] * t / self.fs)

        composite_frbm = final_sonic + final_super
        
        print(f"FRBM Composite Signal Generated.")
        return composite_frbm

# Simulation
if __name__ == "__main__":
    mod = FractalBasebandModulator()
    # Mock Data Streams
    bits_a = np.random.randint(0, 2, 10000)
    bits_b = np.random.randint(0, 2, 50000)
    
    tx_signal = mod.synthesize_fractal(bits_a, bits_b)
