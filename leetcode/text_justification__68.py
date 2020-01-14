def min_line_length(words: List[str]):
    return sum(len(word) for word in words) + (len(words)-1)
 
def word_line_length(words: List[str]):
    return sum(len(word) for word in words)

def format_line(line, max_width):
    if len(line) == 1:
        spaces = " " * (max_width - len(line[0]))
        return line[0] + spaces
    
    total_spaces = max_width - word_line_length(line)
    space_slots = max(len(line)-1, 1)
    per_word_spaces = total_spaces // space_slots
    extra_spaces = total_spaces % space_slots
    
    formatted_line = []
    for word in line[:-1]:
        extra_space = int(extra_spaces > 0)
        formatted_line.extend((word, " " * (per_word_spaces + extra_space)))
        extra_spaces -= 1
    formatted_line.append(line[-1])
    return "".join(formatted_line)

class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        next_word = 0
        unformatted_lines = []
        while next_word < len(words):
            line = []
            while next_word < len(words) and min_line_length(line + [words[next_word]]) <= max_width:
                line.append(words[next_word])
                next_word += 1
            unformatted_lines.append(line)
        
        formatted_lines = []
        for line in unformatted_lines[:-1]:
            formatted_lines.append(format_line(line, max_width))
        
        final_line_words = " ".join(unformatted_lines[-1])
        last_line = final_line_words + " " * (max_width - len(final_line_words))
        formatted_lines.append(last_line)
        return formatted_lines
        
