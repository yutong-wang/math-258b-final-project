# A wrapper for the LattE integrale count functionction without installing latte_int Sage package.


# REQUIRES P_cdd, a cdd file representation of the polytope
# REQUIRES the precompiled LattE "count" program to be placed in the same folder.
# RETURNS the number of integral points inside the polytope
def integral_points_count(P_latte):
        from subprocess import Popen, PIPE
	latte_proc = Popen(['./bin/count', '--cdd','/dev/stdin'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

	latte_proc.stdin.write(P_latte)
	output, err = latte_proc.communicate()
	latte_proc.stdin.close()
	if len(output)>0:
		# print output
		outs = [s.strip() for s in output.splitlines()]
		return int(outs[-1])
	else:
		if err.split('\n')[-2] == "The number of lattice points is 1.":
			return 1
		else:
			return 0
"""
# Remove stuff below later

# If there is > 1 points, then output is not length 0 and we can use that
# If there is 1 point, then output has length 0, and the err says there is 1 lattice point.
# If there is 0 point, then output has length 0, and the err says there is 1 lattice point.
def integral_points_count_latte():
        from subprocess import Popen, PIPE, STDOUT
	latte_proc = Popen(['./count', 'sample_latte_file/empty', ], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	output, err = latte_proc.communicate()
	return None
"""


