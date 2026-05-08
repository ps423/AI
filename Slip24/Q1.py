'''
Q.1) Build a bot which provides all the information related to you in college
[10 Marks]
'''

def college_info_bot():
    print("Welcome to College Information Bot!")
    print("I can provide information about: courses, faculty, facilities, admission, events")
    
    while True:
        query = input("\nWhat would you like to know? (type 'exit' to quit): ").lower()
        
        if 'course' in query:
            print("We offer: Computer Science, IT, Electronics, Mechanical Engineering")
        elif 'faculty' in query or 'teacher' in query:
            print("We have experienced faculty with PhDs and industry experience")
        elif 'facilit' in query:
            print("Facilities: Library, Labs, Sports complex, Hostels, Cafeteria")
        elif 'admission' in query:
            print("Admission process: Apply online, Entrance test, Interview")
        elif 'event' in query:
            print("Upcoming events: Tech fest, Cultural festival, Sports meet")
        elif 'exit' in query or 'quit' in query:
            print("Thank you for using College Information Bot!")
            break
        else:
            print("I can provide information about: courses, faculty, facilities, admission, events")

college_info_bot()
