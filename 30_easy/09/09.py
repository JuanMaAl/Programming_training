# 9. Count Ocurrences of a substring

def count_substring(source_str, substr):
	number_of_times = source_str.count(substr)
	return number_of_times

source_str = "Un triste tigre, Dos tristes tigres, Tres tristes tigres  coment trigo en un trigal"
substr = "tri"
print(count_substring(source_str, substr))
