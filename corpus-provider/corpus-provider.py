


text_corpus = '''
In parallel computing, an embarrassingly parallel workload or problem (also called embarrassingly parallelizable, 
perfectly parallel, delightfully parallel or pleasingly parallel) is one where little or no effort is needed to separate 
the problem into a number of parallel tasks. This is often the case where there is little or no dependency or need for 
communication between those parallel tasks, or for results between them. Thus, these are different from distributed 
computing problems that need communication between tasks, especially communication of intermediate results. They are easy 
to perform on server farms which lack the special infrastructure used in a true supercomputer cluster. They are thus 
well suited to large, Internet-based distributed platforms such as BOINC, and do not suffer from parallel slowdown. 
The opposite of embarrassingly parallel problems are inherently serial problems, which cannot be parallelized at all.
A common example of an embarrassingly parallel problem is 3D video rendering handled by a graphics processing unit, 
where each frame (forward method) or pixel (ray tracing method) can be handled with no interdependency.
Some forms of password cracking are another embarrassingly parallel task that is easily distributed on central 
processing units, CPU cores, or clusters.
'''

import json
outs = {}
with open('/tmp/text_corpus.txt', 'w') as file_text_corpus:
    file_text_corpus.write(text_corpus)
print(json.dumps(outs))
