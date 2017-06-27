import itertools

nums = [x for x in range(1, 10)]
#全排列函数, 筛选出和为15的
sequence_3num = [p for p in itertools.permutations(nums, 3) if sum(p) == 15] 

#循环列出所有矩阵
for row1_1, row1_2, row1_3 in sequence_3num:
	for row2_1, row2_2, row2_3 in sequence_3num:
		for row3_1, row3_2, row3_3 in sequence_3num:
			#筛选出符合要求的矩阵
			if row1_1 + row1_2 + row1_3 == 15 \
				and row2_1 + row2_2 + row2_3 == 15 \
				and row3_1 + row3_2 + row3_3 == 15 \
				and row1_1 + row2_1 + row3_1 == 15 \
				and row1_2 + row2_2 + row3_2 == 15 \
				and row1_3 + row2_3 + row3_3 == 15 \
				and row1_1 + row2_2 + row3_3 == 15 \
				and row1_3 + row2_2 + row3_1 == 15:

				#利用集合去重
				row1 = set([row1_1, row1_2, row1_3])
				row2 = set([row2_1, row2_2, row2_3])
				if len(row1 & row2) == 0:
					print(row1_1, row1_2, row1_3, row2_1, row2_2, row2_3, row3_1, row3_2, row3_3)
				

