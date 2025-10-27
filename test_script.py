import sys
sys.path.append('app')
from model_utils import score_resume_against_jd
resume = 'Software Engineer with 5 years of experience in Python, Flask, machine learning, and data analysis.'
jd = 'We are seeking a Python developer with experience in Flask, machine learning, and web application development.'
score, matches = score_resume_against_jd(resume, jd)
print('Score:', score)
print('Matches:', matches)
print('Matches joined:', ', '.join(matches))
print('Score formatted:', f'{score:.3f}')
print('Score type:', type(score))
print('Matches type:', type(matches))
print('Matches[0] type:', type(matches[0]))
print('Matches joined type:', type(', '.join(matches)))
print('Score == 0.0:', score == 0.0)
print('Score > 0:', score > 0)
print('Matches len:', len(matches))
print('Matches joined len:', len(', '.join(matches)))
print('Matches joined:', repr(', '.join(matches)))
print('Score formatted:', repr(f'{score:.3f}'))
print('Score formatted type:', type(f'{score:.3f}'))
print('Score formatted == "0.000":', f'{score:.3f}' == '0.000')
