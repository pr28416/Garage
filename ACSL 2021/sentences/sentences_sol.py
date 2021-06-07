def generate_sentences(dictionary, sentences):
    partsOfSpeech = {"N": [[], 0], "C": [[], 0], "V": [[], 0], "J": [[], 0], "B": [[], 0], "P": [[], 0]}
    typesSentence = {"D": ["", "."], "I": ["", "."], "Q": ["What ", "?"], "E": ["", "!"]}
    for line in dictionary:
        partsOfSpeech[line[0]][0] = line[2:].split(" ")
    phrases = sentences.split(" ")
    answers = []
    for phrase in phrases:
        string_blocks, prefix, suffix = [], "", ""
        for idx, char in enumerate(phrase):
            if idx == 0:
                prefix, suffix = typesSentence[char][0], typesSentence[char][1]
            else:
                if char in partsOfSpeech:
                    string_blocks.append(partsOfSpeech[char][0][partsOfSpeech[char][1]])
                    partsOfSpeech[char][1] = (partsOfSpeech[char][1] + 1) % len(partsOfSpeech[char][0])
                elif char == "A":
                    nextChar = phrase[idx+1]
                    if partsOfSpeech[nextChar][0][partsOfSpeech[nextChar][1]][0] in {'a', 'e', 'i', 'o', 'u'}:
                        string_blocks.append("an")
                    else:
                        string_blocks.append("a")
                else: # char == "T"
                    string_blocks.append("the")
        sent = prefix + " ".join(string_blocks) + suffix
        sent = sent[0].upper() + sent[1:]
        answers.append(sent)
    return " ".join(answers)