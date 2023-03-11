text = 'X-DSPAM-Confidence:     0.8475'
cut = text.find(':')
final = text[cut+1:]
print(float(final))
