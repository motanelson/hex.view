def visualize_hex(input_file, output_file):
    try:
        with open(input_file, "rb") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            offset = 0  # Offset inicial

            while True:
                # Lê até 16 bytes por vez
                chunk = infile.read(16)
                if not chunk:
                    break

                # Convertendo bytes para valores hexadecimais
                hex_values = " ".join(f"{byte:02X}" for byte in chunk)

                # Criando os caracteres legíveis (ou substituindo por '.')
                ascii_values = "".join(
                    chr(byte) if 32 <= byte <= 127 else "." for byte in chunk
                )

                # Escrevendo a linha formatada no arquivo de saída
                outfile.write(
                    f"{hex_values:<47} ; {offset:08X} {ascii_values}\n"
                )

                # Incrementando o offset
                offset += len(chunk)

        print(f"Hex dump successfully saved to: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except IOError as e:
        print(f"Error reading or writing files: {e}")


def main():
    input_file = input("Enter the input file name: ").strip()
    output_file = input_file + ".hex"  # Nome do arquivo de saída

    visualize_hex(input_file, output_file)


if __name__ == "__main__":
    main()

