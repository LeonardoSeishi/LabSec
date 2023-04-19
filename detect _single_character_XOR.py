from challenge3_only_function import testing_keys, singlebyte_xor

file = open("texts.txt", 'r')

line = file.readline()              #read the firt line
best_score = testing_keys(line)     #variable that saves the best score of all lines
line_i = 1                          #iterator
best_line = line_i                  #save the line of the answer


while line != "":   #read all the lines until the end
    line_i += 1
    line = file.readline()
    current_score = testing_keys(line)   #return a tuple with the key and the score of each line
    if current_score[1] < best_score[1]: #check for the a lower score
        best_score = current_score
        best_line = line_i
        text = line

print(f'text : {singlebyte_xor(bytes.fromhex(text), best_score[0])}\nscore: {best_score[1]}\nkey: {hex(best_score[0])}\nline: {best_line}')
