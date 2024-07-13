using Miningcore.Contracts;
using Miningcore.Native;

namespace Miningcore.Crypto.Hashing.Algorithms;

[Identifier("eaglesong")]
public unsafe class Eaglesong : IHashAlgorithm
{
    public void Digest(ReadOnlySpan<byte> data, Span<byte> result, params object[] extra)
    {
        // Ensure the input data is of the correct length
        Contract.Requires<ArgumentException>(data.Length == 80);
        // Ensure the output result buffer is of the correct length
        Contract.Requires<ArgumentException>(result.Length >= 32);

        // Use fixed keyword to pin the input and output buffers in memory
        fixed (byte* input = data)
        {
            fixed (byte* output = result)
            {
                // Call the native eaglesong hash function
                Multihash.blake(input, output, (uint)data.Length);
            }
        }
    }
}