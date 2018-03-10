ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        }, {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

email = ramit.get('email')
print email
interests = ramit.get("interests")[0]
print interests
jas = ramit['friends'][0]['email']
print jas
janint = ramit['friends'][1]['interests'][1]
print janint


