from itertools import combinations
import itertools

strings =  [['merged_chr1_1000.vcf.gz'],['--out-prefix','out'],['--out-prefix','res'],['--out-format','removed_sites'],['--out-format','kept_sites'],['--out-format','vcf'],['--out-format','bcf'],['--filter-min-alleles', '2'],['--filter-max-alleles', '4']]

filList1 = []
comb = []

for i in range(len(strings)):

    b = list(combinations(strings, i+1))
    c = map(list, b)
    comb.append(c)

whole_list = []

for x in comb:
    for y in x:
        b = list(itertools.chain.from_iterable(y))
        whole_list.append(b)
                #print b
m = whole_list


def filFunc(name, lol, listname):
    for x in lol:
        for y in x:
            if y== name:
                listname.append(x) 
                
filFunc('merged_chr1_1000.vcf.gz', m, filList1)
fnameFilter = filList1
#print fnameFilter
print "--------------"


app = []
for m in fnameFilter:
    
    for x,y in itertools.combinations(m, 2):
        #print x,y
        if x == y:
           app.append(m) 
#print app
        
unmatched = [d for d in fnameFilter if d not in app]

for t in unmatched:
    print t
