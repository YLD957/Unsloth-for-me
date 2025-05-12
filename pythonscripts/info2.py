# import json

# def process_info_to_qa(file_path, output_path):
#     """
#     Converts the content of info.txt into a structured Q&A JSON format.
    
#     Args:
#         file_path (str): Path to the input txt file.
#         output_path (str): Path to save the output JSON file.
#     """
#     with open(file_path, "r", encoding="utf-8") as file:
#         content = file.readlines()
    
#     # Initialize storage for question-answer pairs
#     qa_list = []
#     current_question = None
#     current_answer = []

#     for line in content:
#         line = line.strip()
        
#         if not line:
#             # Skip empty lines
#             continue
        
#         # Check if the line is a title (e.g., "2.1 北京联合大学人工智能专业选科要求")
#         if line[0].isdigit() and (" " in line or "." in line[:5]):
#             # Save the previous Q&A pair
#             if current_question:
#                 qa_list.append({
#                     "question": current_question,
#                     "answer": "\n".join(current_answer).strip()
#                 })
            
#             # Start a new question
#             current_question = line
#             current_answer = []
#         else:
#             # Otherwise, accumulate the answer text
#             current_answer.append(line)
    
#     # Add the last Q&A pair
#     if current_question:
#         qa_list.append({
#             "question": current_question,
#             "answer": "\n".join(current_answer).strip()
#         })
    
#     # Save the Q&A format as JSON
#     with open(output_path, "w", encoding="utf-8") as json_file:
#         json.dump(qa_list, json_file, ensure_ascii=False, indent=4)

#     print(f"Processed Q&A data has been saved to {output_path}")


# # File paths
# input_file = "info2.txt"
# output_file = "qa_data.json"

# # Process the file
# process_info_to_qa(input_file, output_file)

import json

def convert_qa_to_conversations(input_file, output_file):
    """
    将问答格式JSON文件转换为对话格式JSON文件
    
    Args:
        input_file (str): 输入JSON文件路径（包含问答对）
        output_file (str): 输出JSON文件路径（转换后的对话格式）
    """
    # 1. 读取原始问答JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        qa_data = json.load(f)
    
    # 2. 转换数据格式
    converted_data = []
    
    # 处理单条问答的情况（直接是字典）
    if isinstance(qa_data, dict):
        converted_data.append({
            'conversations': [
                {'content': qa_data['question'], 'role': 'user'},
                {'content': qa_data['answer'], 'role': 'assistant'}
            ],
            'source': 'custom-source',  # 可自定义
            'score': 5.0               # 可自定义评分
        })
    # 处理多条问答的情况（列表形式）
    elif isinstance(qa_data, list):
        for item in qa_data:
            converted_data.append({
                'conversations': [
                    {'content': item['question'], 'role': 'user'},
                    {'content': item['answer'], 'role': 'assistant'}
                ],
                'source': 'custom-source',
                'score': 5.0
            })
    
    # 3. 保存转换后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=2)
    
    print(f"转换完成！已保存到 {output_file}")

# 使用示例
if __name__ == "__main__":
    # 输入文件（假设是包含问答对的JSON）
    input_json = "qa_data.json" 
    # 输出文件（转换后的对话格式）
    output_json = "conversations.json"
    
    convert_qa_to_conversations(input_json, output_json)
