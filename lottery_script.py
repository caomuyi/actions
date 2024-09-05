import hashlib
import time

# 最大回复编号id
total_replies = 500
# 每100分组
group_size = 100
# 使用当前时间戳作为随机元素
current_time = str(time.time())
random_element = hashlib.sha256(current_time.encode()).hexdigest()

# 每个组的获奖者
winners = []

for i in range(0, total_replies, group_size):
    # 当前组的回复 ID 范围
    current_group = list(range(i + 1, i + group_size + 1))
    
    # 拼接当前组的所有回复 ID 和随机元素
    combined_string = ''.join(map(str, current_group)) + random_element
    
    # 使用 SHA-256 哈希函数将拼接的字符串进行哈希
    hash_object = hashlib.sha256(combined_string.encode())
    hash_hex = hash_object.hexdigest()
    
    # 将哈希值转换为一个正整数
    hash_int = int(hash_hex, 16)
    
    # 使用哈希值对组内的回复 ID 数量取模，得到一个随机索引
    winner_index = hash_int % group_size
    
    # 确定组内的获奖者 ID
    winner = current_group[winner_index]
    winners.append(winner)

print("获奖者是", winners)
