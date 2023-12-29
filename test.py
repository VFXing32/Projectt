def format_text(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')

    # Initialize an empty list to store the formatted lines
    formatted_lines = []

    # Iterate through the lines
    for line in lines:
        # Check if the line contains "},"
        if "}," in line:
            # Add a new line after "},"
            formatted_lines.append(line.replace("},", "},\n"))
        else:
            # If the line doesn't contain "}," as it is
            formatted_lines.append(line)

    # Join the formatted lines to get the final result
    formatted_text = '\n'.join(formatted_lines)

    return formatted_text

# Input text
input_text = '{"tilemap": {"9;12": {"type": "grass", "variant": 2, "pos": [9, 12]}, "9;13": {"type": "grass", "variant": 8, "pos": [9, 13]}, "10;13": {"type": "grass", "variant": 1, "pos": [10, 13]}, "11;13": {"type": "grass", "variant": 1, "pos": [11, 13]}, "12;13": {"type": "grass", "variant": 1, "pos": [12, 13]}, "13;13": {"type": "grass", "variant": 1, "pos": [13, 13]}, "14;13": {"type": "grass", "variant": 1, "pos": [14, 13]}, "15;13": {"type": "grass", "variant": 1, "pos": [15, 13]}, "15;14": {"type": "grass", "variant": 8, "pos": [15, 14]}, "14;14": {"type": "grass", "variant": 8, "pos": [14, 14]}, "13;14": {"type": "grass", "variant": 8, "pos": [13, 14]}, "12;14": {"type": "grass", "variant": 8, "pos": [12, 14]}, "11;14": {"type": "grass", "variant": 8, "pos": [11, 14]}, "10;14": {"type": "grass", "variant": 8, "pos": [10, 14]}, "9;14": {"type": "grass", "variant": 8, "pos": [9, 14]}, "8;14": {"type": "grass", "variant": 8, "pos": [8, 14]}, "7;14": {"type": "grass", "variant": 8, "pos": [7, 14]}, "8;15": {"type": "grass", "variant": 5, "pos": [8, 15]}, "9;15": {"type": "grass", "variant": 5, "pos": [9, 15]}, "10;15": {"type": "grass", "variant": 5, "pos": [10, 15]}, "11;15": {"type": "grass", "variant": 5, "pos": [11, 15]}, "12;15": {"type": "grass", "variant": 5, "pos": [12, 15]}, "13;15": {"type": "grass", "variant": 5, "pos": [13, 15]}, "14;15": {"type": "grass", "variant": 5, "pos": [14, 15]}, "15;15": {"type": "grass", "variant": 5, "pos": [15, 15]}, "7;15": {"type": "grass", "variant": 6, "pos": [7, 15]}, "8;13": {"type": "grass", "variant": 8, "pos": [8, 13]}, "7;13": {"type": "grass", "variant": 8, "pos": [7, 13]}, "7;12": {"type": "grass", "variant": 8, "pos": [7, 12]}, "8;12": {"type": "grass", "variant": 8, "pos": [8, 12]}, "7;11": {"type": "grass", "variant": 1, "pos": [7, 11]}, "8;11": {"type": "grass", "variant": 2, "pos": [8, 11]}, "6;11": {"type": "grass", "variant": 1, "pos": [6, 11]}, "5;11": {"type": "grass", "variant": 1, "pos": [5, 11]}, "4;11": {"type": "grass", "variant": 1, "pos": [4, 11]}, "3;11": {"type": "grass", "variant": 1, "pos": [3, 11]}, "2;11": {"type": "grass", "variant": 1, "pos": [2, 11]}, "1;11": {"type": "grass", "variant": 1, "pos": [1, 11]}, "1;12": {"type": "grass", "variant": 8, "pos": [1, 12]}, "2;12": {"type": "grass", "variant": 8, "pos": [2, 12]}, "2;13": {"type": "grass", "variant": 8, "pos": [2, 13]}, "3;13": {"type": "grass", "variant": 8, "pos": [3, 13]}, "4;13": {"type": "grass", "variant": 8, "pos": [4, 13]}, "4;14": {"type": "grass", "variant": 5, "pos": [4, 14]}, "5;14": {"type": "grass", "variant": 5, "pos": [5, 14]}, "6;14": {"type": "grass", "variant": 5, "pos": [6, 14]}, "3;14": {"type": "grass", "variant": 5, "pos": [3, 14]}, "2;14": {"type": "grass", "variant": 5, "pos": [2, 14]}, "1;14": {"type": "grass", "variant": 6, "pos": [1, 14]}, "1;13": {"type": "grass", "variant": 8, "pos": [1, 13]}, "3;12": {"type": "grass", "variant": 8, "pos": [3, 12]}, "4;12": {"type": "grass", "variant": 8, "pos": [4, 12]}, "5;12": {"type": "grass", "variant": 8, "pos": [5, 12]}, "6;12": {"type": "grass", "variant": 8, "pos": [6, 12]}, "6;13": {"type": "grass", "variant": 8, "pos": [6, 13]}, "5;13": {"type": "grass", "variant": 8, "pos": [5, 13]}, "0;13": {"type": "grass", "variant": 6, "pos": [0, 13]}, "0;12": {"type": "grass", "variant": 7, "pos": [0, 12]}, "0;11": {"type": "grass", "variant": 0, "pos": [0, 11]}, "16;13": {"type": "grass", "variant": 8, "pos": [16, 13]}, "16;12": {"type": "grass", "variant": 0, "pos": [16, 12]}, "17;12": {"type": "grass", "variant": 8, "pos": [17, 12]}, "17;11": {"type": "grass", "variant": 0, "pos": [17, 11]}, "18;11": {"type": "grass", "variant": 8, "pos": [18, 11]}, "18;10": {"type": "grass", "variant": 0, "pos": [18, 10]}, "19;10": {"type": "grass", "variant": 1, "pos": [19, 10]}, "20;10": {"type": "grass", "variant": 1, "pos": [20, 10]}, "16;15": {"type": "grass", "variant": 5, "pos": [16, 15]}, "17;15": {"type": "grass", "variant": 4, "pos": [17, 15]}, "18;14": {"type": "grass", "variant": 5, "pos": [18, 14]}, "19;14": {"type": "grass", "variant": 5, "pos": [19, 14]}, "20;14": {"type": "grass", "variant": 5, "pos": [20, 14]}, "21;14": {"type": "grass", "variant": 5, "pos": [21, 14]}, "22;14": {"type": "grass", "variant": 4, "pos": [22, 14]}, "22;13": {"type": "grass", "variant": 8, "pos": [22, 13]}, "23;13": {"type": "grass", "variant": 5, "pos": [23, 13]}, "24;13": {"type": "grass", "variant": 4, "pos": [24, 13]}, "24;12": {"type": "grass", "variant": 3, "pos": [24, 12]}, "24;11": {"type": "grass", "variant": 3, "pos": [24, 11]}, "24;10": {"type": "grass", "variant": 2, "pos": [24, 10]}, "23;10": {"type": "grass", "variant": 1, "pos": [23, 10]}, "22;10": {"type": "grass", "variant": 1, "pos": [22, 10]}, "21;10": {"type": "grass", "variant": 1, "pos": [21, 10]}, "23;11": {"type": "grass", "variant": 8, "pos": [23, 11]}, "23;12": {"type": "grass", "variant": 8, "pos": [23, 12]}, "22;12": {"type": "grass", "variant": 8, "pos": [22, 12]}, "21;12": {"type": "grass", "variant": 8, "pos": [21, 12]}, "21;11": {"type": "grass", "variant": 8, "pos": [21, 11]}, "20;11": {"type": "grass", "variant": 8, "pos": [20, 11]}, "19;11": {"type": "grass", "variant": 8, "pos": [19, 11]}, "18;12": {"type": "grass", "variant": 8, "pos": [18, 12]}, "17;13": {"type": "grass", "variant": 8, "pos": [17, 13]}, "16;14": {"type": "grass", "variant": 8, "pos": [16, 14]}, "18;13": {"type": "grass", "variant": 8, "pos": [18, 13]}, "19;13": {"type": "grass", "variant": 8, "pos": [19, 13]}, "19;12": {"type": "grass", "variant": 8, "pos": [19, 12]}, "20;12": {"type": "grass", "variant": 8, "pos": [20, 12]}, "22;11": {"type": "grass", "variant": 8, "pos": [22, 11]}, "21;13": {"type": "grass", "variant": 8, "pos": [21, 13]}, "20;13": {"type": "grass", "variant": 8, "pos": [20, 13]}, "17;14": {"type": "grass", "variant": 8, "pos": [17, 14]}, "19;4": {"type": "grass", "variant": 1, "pos": [19, 4]}, "18;4": {"type": "grass", "variant": 1, "pos": [18, 4]}, "17;4": {"type": "grass", "variant": 0, "pos": [17, 4]}, "17;5": {"type": "grass", "variant": 8, "pos": [17, 5]}, "16;5": {"type": "grass", "variant": 0, "pos": [16, 5]}, "16;6": {"type": "grass", "variant": 6, "pos": [16, 6]}, "17;6": {"type": "grass", "variant": 5, "pos": [17, 6]}, "18;6": {"type": "grass", "variant": 5, "pos": [18, 6]}, "19;6": {"type": "grass", "variant": 4, "pos": [19, 6]}, "19;5": {"type": "grass", "variant": 8, "pos": [19, 5]}, "20;5": {"type": "grass", "variant": 4, "pos": [20, 5]}, "20;4": {"type": "grass", "variant": 2, "pos": [20, 4]}, "18;5": {"type": "grass", "variant": 8, "pos": [18, 5]}, "8;5": {"type": "grass", "variant": 2, "pos": [8, 5]}, "7;5": {"type": "grass", "variant": 1, "pos": [7, 5]}, "6;5": {"type": "grass", "variant": 0, "pos": [6, 5]}, "6;6": {"type": "grass", "variant": 6, "pos": [6, 6]}, "7;6": {"type": "grass", "variant": 8, "pos": [7, 6]}, "7;7": {"type": "grass", "variant": 6, "pos": [7, 7]}, "8;7": {"type": "grass", "variant": 5, "pos": [8, 7]}, "9;7": {"type": "grass", "variant": 4, "pos": [9, 7]}, "9;6": {"type": "grass", "variant": 2, "pos": [9, 6]}, "8;6": {"type": "grass", "variant": 8, "pos": [8, 6]}, "26;8": {"type": "stone", "variant": 0, "pos": [26, 8]}, "26;9": {"type": "stone", "variant": 7, "pos": [26, 9]}, "26;10": {"type": "stone", "variant": 7, "pos": [26, 10]}, "26;11": {"type": "stone", "variant": 6, "pos": [26, 11]}, "27;12": {"type": "stone", "variant": 7, "pos": [27, 12]}, "27;13": {"type": "stone", "variant": 6, "pos": [27, 13]}, "28;13": {"type": "stone", "variant": 5, "pos": [28, 13]}, "29;13": {"type": "stone", "variant": 4, "pos": [29, 13]}, "29;12": {"type": "stone", "variant": 8, "pos": [29, 12]}, "30;12": {"type": "stone", "variant": 4, "pos": [30, 12]}, "30;11": {"type": "stone", "variant": 3, "pos": [30, 11]}, "30;10": {"type": "stone", "variant": 3, "pos": [30, 10]}, "30;9": {"type": "stone", "variant": 3, "pos": [30, 9]}, "30;8": {"type": "stone", "variant": 2, "pos": [30, 8]}, "27;8": {"type": "stone", "variant": 1, "pos": [27, 8]}, "28;9": {"type": "stone", "variant": 8, "pos": [28, 9]}, "28;10": {"type": "stone", "variant": 8, "pos": [28, 10]}, "28;11": {"type": "stone", "variant": 8, "pos": [28, 11]}, "28;8": {"type": "stone", "variant": 1, "pos": [28, 8]}, "29;9": {"type": "stone", "variant": 8, "pos": [29, 9]}, "29;8": {"type": "stone", "variant": 1, "pos": [29, 8]}, "29;10": {"type": "stone", "variant": 8, "pos": [29, 10]}, "29;11": {"type": "stone", "variant": 8, "pos": [29, 11]}, "28;12": {"type": "stone", "variant": 8, "pos": [28, 12]}, "27;11": {"type": "stone", "variant": 8, "pos": [27, 11]}, "27;10": {"type": "stone", "variant": 8, "pos": [27, 10]}, "27;9": {"type": "stone", "variant": 8, "pos": [27, 9]}, "23;9": {"type": "decor", "variant": 0, "pos": [23, 9]}, "13;12": {"type": "decor", "variant": 0, "pos": [13, 12]}, "7;10": {"type": "decor", "variant": 0, "pos": [7, 10]}, "5;10": {"type": "decor", "variant": 0, "pos": [5, 10]}, "2;10": {"type": "decor", "variant": 0, "pos": [2, 10]}, "7;4": {"type": "decor", "variant": 0, "pos": [7, 4]}, "8;4": {"type": "decor", "variant": 1, "pos": [8, 4]}, "17;3": {"type": "decor", "variant": 1, "pos": [17, 3]}, "22;9": {"type": "decor", "variant": 1, "pos": [22, 9]}, "15;12": {"type": "decor", "variant": 1, "pos": [15, 12]}, "10;12": {"type": "decor", "variant": 1, "pos": [10, 12]}, "8;10": {"type": "decor", "variant": 1, "pos": [8, 10]}, "3;10": {"type": "decor", "variant": 1, "pos": [3, 10]}, "1;10": {"type": "decor", "variant": 2, "pos": [1, 10]}, "6;10": {"type": "decor", "variant": 2, "pos": [6, 10]}, "12;12": {"type": "decor", "variant": 2, "pos": [12, 12]}, "9;5": {"type": "decor", "variant": 2, "pos": [9, 5]}, "19;3": {"type": "decor", "variant": 2, "pos": [19, 3]}, "21;9": {"type": "spawners", "variant": 1, "pos": [21, 9]}, "19;9": {"type": "decor", "variant": 3, "pos": [19, 9]}, "6;4": {"type": "decor", "variant": 3, "pos": [6, 4]}, "27;7": {"type": "decor", "variant": 3, "pos": [27, 7]}, "33;5": {"type": "stone", "variant": 0, "pos": [33, 5]}, "33;6": {"type": "stone", "variant": 7, "pos": [33, 6]}, "33;7": {"type": "stone", "variant": 6, "pos": [33, 7]}, "34;8": {"type": "stone", "variant": 6, "pos": [34, 8]}, "35;8": {"type": "stone", "variant": 5, "pos": [35, 8]}, "36;8": {"type": "stone", "variant": 5, "pos": [36, 8]}, "37;8": {"type": "stone", "variant": 5, "pos": [37, 8]}, "38;8": {"type": "stone", "variant": 5, "pos": [38, 8]}, "39;8": {"type": "stone", "variant": 4, "pos": [39, 8]}, "34;6": {"type": "stone", "variant": 8, "pos": [34, 6]}, "34;7": {"type": "stone", "variant": 8, "pos": [34, 7]}, "35;7": {"type": "stone", "variant": 8, "pos": [35, 7]}, "36;7": {"type": "stone", "variant": 8, "pos": [36, 7]}, "37;7": {"type": "stone", "variant": 8, "pos": [37, 7]}, "38;7": {"type": "stone", "variant": 8, "pos": [38, 7]}, "39;7": {"type": "stone", "variant": 8, "pos": [39, 7]}, "40;7": {"type": "stone", "variant": 5, "pos": [40, 7]}, "35;6": {"type": "stone", "variant": 8, "pos": [35, 6]}, "36;6": {"type": "stone", "variant": 8, "pos": [36, 6]}, "37;6": {"type": "stone", "variant": 8, "pos": [37, 6]}, "38;6": {"type": "stone", "variant": 8, "pos": [38, 6]}, "39;6": {"type": "stone", "variant": 8, "pos": [39, 6]}, "40;6": {"type": "stone", "variant": 8, "pos": [40, 6]}, "34;5": {"type": "stone", "variant": 1, "pos": [34, 5]}, "35;5": {"type": "stone", "variant": 1, "pos": [35, 5]}, "36;5": {"type": "stone", "variant": 1, "pos": [36, 5]}, "37;5": {"type": "stone", "variant": 1, "pos": [37, 5]}, "38;5": {"type": "stone", "variant": 1, "pos": [38, 5]}, "39;5": {"type": "stone", "variant": 1, "pos": [39, 5]}, "40;4": {"type": "stone", "variant": 0, "pos": [40, 4]}, "41;4": {"type": "stone", "variant": 1, "pos": [41, 4]}, "42;4": {"type": "stone", "variant": 2, "pos": [42, 4]}, "42;5": {"type": "stone", "variant": 4, "pos": [42, 5]}, "41;6": {"type": "stone", "variant": 3, "pos": [41, 6]}, "41;7": {"type": "stone", "variant": 4, "pos": [41, 7]}, "40;5": {"type": "stone", "variant": 8, "pos": [40, 5]}, "41;5": {"type": "stone", "variant": 8, "pos": [41, 5]}}, "tile_size": 16, "offgrid": [{"type": "large_decor", "variant": 0, "pos": [457.0, 119.0]}, {"type": "large_decor", "variant": 0, "pos": [361.5, 151.0]}, {"type": "large_decor", "variant": 0, "pos": [70.0, 167.5]}, {"type": "large_decor", "variant": 1, "pos": [278.5, 165.5]}, {"type": "large_decor", "variant": 1, "pos": [293.5, 149.0]}, {"type": "large_decor", "variant": 1, "pos": [133.0, 180.0]}, {"type": "large_decor", "variant": 1, "pos": [4.0, 165.5]}, {"type": "large_decor", "variant": 2, "pos": [25.0, 133.0]}, {"type": "large_decor", "variant": 2, "pos": [170.5, 166.0]}, {"type": "large_decor", "variant": 2, "pos": [239.0, 188.5]}, {"type": "large_decor", "variant": 2, "pos": [252.5, 37.0]}, {"type": "large_decor", "variant": 2, "pos": [118.0, 37.5]}, {"type": "large_decor", "variant": 2, "pos": [340.0, 117.0]}, {"type": "spawners", "variant": 0, "pos": [228.5, 192.5]}, {"type": "spawners", "variant": 1, "pos": [59.5, 159.5]}]}'

# Call the function to format the text
formatted_text = format_text(input_text)

# Print the formatted text
print(formatted_text)
