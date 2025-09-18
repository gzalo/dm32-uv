import os
import re

def combine_wavs_to_bin(input_dir, output_file):
    # Regex to capture addresses like 0x1ee00.wav
    addr_re = re.compile(r".*\.0x([0-9a-fA-F]+)\..*$")

    # Collect (address, filename, size)
    chunks = []
    for fname in os.listdir(input_dir):
        match = addr_re.match(fname)
        if match:
            addr = int(match.group(1), 16)
            fpath = os.path.join(input_dir, fname)
            size = os.path.getsize(fpath)
            chunks.append((addr, fpath, size))

    if not chunks:
        print("No valid .wav files found.")
        return

    # Sort by address
    chunks.sort(key=lambda x: x[0])

    # Check overlaps and gaps
    issues = []
    for i in range(len(chunks) - 1):
        addr, _, size = chunks[i]
        next_addr, _, _ = chunks[i + 1]
        end_addr = addr + size
        if end_addr > next_addr:
            issues.append(f"Overlap between {hex(addr)} and {hex(next_addr)}")
        elif next_addr - end_addr > 4:  # Only complain if gap > 4 bytes
            issues.append(f"Gap of {next_addr - end_addr} bytes between {hex(end_addr)} and {hex(next_addr)}")

    if issues:
        print("Issues detected:")
        for issue in issues:
            print("  " + issue)
    else:
        print("No significant overlaps or gaps detected.")

    # Allocate full buffer
    max_addr = max(addr + size for addr, _, size in chunks)
    buffer = bytearray(max_addr)

    # Write each file into buffer
    for addr, fpath, size in chunks:
        with open(fpath, "rb") as f:
            data = f.read()
        buffer[addr:addr+size] = data

    # Save combined .bin file
    with open(output_file, "wb") as out:
        out.write(buffer)

    print(f"Combined file written to {output_file}, size {len(buffer)} bytes.")


if __name__ == "__main__":
    combine_wavs_to_bin("dm32_wav_mod", "mod.enc")
