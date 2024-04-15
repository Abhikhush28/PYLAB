# [11:08 AM] N Murugadoss (Unverified)
student_data = {

    'id1': {

        'name': ['Sara'],

        'class': ['V'],

        'subject_integration': ['english, math, science']

    },

    'id2': {

        'name': ['David'],

        'class': ['V'],

        'subject_integration': ['english, math, science']

    },

    'id3': {

        'name': ['Sara'],

        'class': ['V'],

        'subject_integration': ['english, math, science']

    },

    'id4': {

        'name': ['Surya'],

        'class': ['V'],

        'subject_integration': ['english, math, science']

    }

}
 
# Create an empty dictionary 'result' to store unique student records.
 
result = {}
 
for key, value in student_data.items():

    if value not in result.values():

        result[key] = value
 
# Print the 'result' dictionary containing unique student records.
 
print(result)
