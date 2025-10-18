import re
import csv

# 读取文件内容
with open('professor_list.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用空行分割不同人员的信息块
people_blocks = re.split(r'\n\s*\n', content.strip())

# 准备写入CSV文件
with open('info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Email', 'Research Interests']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # 写入表头
    
    for block in people_blocks:
        # 分割块内容为行
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        
        # 提取姓名（首行）
        name = lines[0] if lines else ''
        
        # 提取邮箱
        email = ''
        email_match = re.search(r'Email:\s*([^\s]+)', block)
        if email_match:
            email = email_match.group(1)
        
        # 提取研究兴趣
        research_interests = ''
        research_match = re.search(r'Research Interests:\s*(.+)', block, re.DOTALL)
        if research_match:
            # 清理研究兴趣中的换行和多余空格
            research_interests = re.sub(r'\s+', ' ', research_match.group(1)).strip()
        
        # 写入CSV行
        writer.writerow({
            'Name': name,
            'Email': email,
            'Research Interests': research_interests
        })

print("数据提取完成，已保存到info.csv")