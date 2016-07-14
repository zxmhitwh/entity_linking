import re

def parser():
	infile = open("dataset/disambiguations_en.tql")
	outfile = open("dataset/disambiguations_en.txt","w")
	#infile = open("dataset/redirects_en.tql")
	#outfile = open("dataset/redirects_en.txt","w")
	line = infile.readline()
	while line:
		line = infile.readline().split()
		if len(line)==5:
			entity1 = line[0].strip("<http://dbpedia.org/resource/").strip(">")
			entity2 = line[2].strip("<http://dbpedia.org/resource/").strip(">")
			strtmp = entity1 + "\t" + entity2 + "\n"
			print strtmp
			outfile.write(strtmp)
		else:
			pass
		line = infile.readline()


if __name__ == '__main__':
	parser()