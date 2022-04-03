def encode(data, max_table_size):
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}

    string = ""
    compressed_data = []

    for symbol in data:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if len(dictionary) <= max_table_size:
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    return compressed_data


def decode(compressed_data: list):
    next_code = 256
    decompressed_data = []
    string = ""

    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + string[0]

        decompressed_data.append(dictionary[code])

        if len(string) != 0:
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1

        string = dictionary[code]

    return "".join(decompressed_data)
