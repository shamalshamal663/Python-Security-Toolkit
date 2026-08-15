import os,random,sys

base_word = ["admin","cypher","root","vault","target_cop"]
suffixes = ["!","@2026","#SEC","$123","!pass"]

def create_payload(words):
    num = random.randint(10,99)
    suffix = random.choice(suffixes)
    payload = f"{words}{num}{suffix}"
    return payload

def export_word_list(output_filename,word_list,count_per_word):
    with open(output_filename,"w") as file:
        for word in word_list:
            for _ in range(count_per_word):
               payload = create_payload(word)
               file.write(f"{payload}\n") 
print("Target Successfully compiled : {output_filename}")


if len(sys.argv) <  2:
    print("Usage:python3 wordlist_builder.py <output_file.txt>")    
    sys.exit()
output_file = sys.argv[1]

export_word_list(output_file,base_word,3)


