def mendel(k, m, n):
    prob_allele_dominant = ( (k*(k-1)*1) + (m*(m-1)*0.75) + (2*k*m*1) + (2*k*n*1) + (2*m*n*0.5) + (n*n*0) ) / ((k+m+n)*(k+m+n-1))
    return prob_allele_dominant

print(mendel(22, 19, 20))