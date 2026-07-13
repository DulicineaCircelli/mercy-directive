import json
import os

def convert_to_jsonl(input_file, output_file):
    dataset = []
    current_conversation = {"messages": []}
    current_role = None
    current_content = []

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.lower().startswith("user:"):
            if current_role:
                current_conversation["messages"].append({"role": current_role, "content": " ".join(current_content)})
            current_role = "user"
            current_content = [line.split(":", 1)[1].strip()]
        
        elif line.lower().startswith("assistant:") or line.lower().startswith("gemini:"):
            if current_role:
                current_conversation["messages"].append({"role": current_role, "content": " ".join(current_content)})
            current_role = "assistant"
            current_content = [line.split(":", 1)[1].strip()]
            
        elif line.startswith("---"):
            if current_role:
                current_conversation["messages"].append({"role": current_role, "content": " ".join(current_content)})
                current_role = None
                current_content = []
            
            if current_conversation["messages"]:
                dataset.append(current_conversation)
                current_conversation = {"messages": []}
        else:
            if current_role:
                current_content.append(line)

    if current_role:
        current_conversation["messages"].append({"role": current_role, "content": " ".join(current_content)})
    if current_conversation["messages"]:
        dataset.append(current_conversation)

    with open(output_file, 'w', encoding='utf-8') as f:
        for convo in dataset:
            f.write(json.dumps(convo) + "\n")
    
    print(f"\n[+] Success! Parsed {len(dataset)} conversation blocks.")
    print(f"[+] Output saved to: {output_file}\n")

input_text = "raw_logs.txt"
output_data = "mercy_directive.jsonl"

if os.path.exists(input_text):
    print(f"Reading {input_text}...")
    convert_to_jsonl(input_text, output_data)
else:
    print(f"Error: Could not find '{input_text}'. Please make sure it is in the same folder as this script.")