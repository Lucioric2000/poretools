import Fast5File
import sys

def run(parser, args):
	
	for fast5 in Fast5File.Fast5FileSet(args.files):
		if args.start_time or args.end_time:
			read_start_time = fast5.get_start_time()
			if args.start_time and args.start_time > read_start_time:
				fast5.close()
				continue
			if args.end_time and args.end_time < read_start_time:
				fast5.close()
				continue

		fas = fast5.get_fastas(args.type)
		for fa in fas:
			if fa is None or \
			len(fa.seq) < args.min_length:			
				fast5.close()
				continue

			print fa

		fast5.close()

