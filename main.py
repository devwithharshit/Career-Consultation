def welcome_message():
    print("Welcome to HSGP Consultations!!")
    print()
    print("If you are at HSGP Consultations, you don't need to worry about your Future!")
    print("At HSGP Consultations, you will get the Best Advice to KickStart your Career!")
    print()

def form_fees():
    print("Now, before you start using our Consultation Services, we want you to Pay the Consultation Fees!")
    print("You have to Pay 49$ to Start Your Consultation!")
    ffp = input("Have you Paid (yes/no)?- ").capitalize()
    return ffp

def get_high_school_stream():
    hstr = input("Enter your High-School Stream (Science, Commerce, or Arts): ")
    return hstr

def provide_stream_motivation(hstr):
    if hstr.capitalize() == "Science":
        print("Science is a Good Stream; you have a lot of Career Options to Opt for!")
        return True
    elif hstr.capitalize() in ["Commerce", "Arts"]:
        print("Commerce & Arts ko hum Advice nahi dete! \nAap Berozgaar hi Rahenge! \nDhanyavaad!")
        return False
    else:
        print("Invalid Stream!")
        return False

def get_career_path():
    tp = input("Do you want to Pursue a career in Medical, Engineering, Research & Philosophy, or be Stream Neutral? ")
    return tp

def provide_career_advice(tp):
    tp = tp.strip().lower()  
    if tp == "medical":
        print("That's Superrb! You are the Future Doctor of our Country!")
    elif tp == "engineering":
        print("That's Superrb! You are the Future Engineer of our Country!")
    elif tp in ["research & philosophy", "rnp"]:
        print("That's Superrb! You are the Future Researcher!")
    elif tp in ["stream neutral", "sn"]:
        print("That's Also Good, you might have a Hobby of yours that you want to Pursue as a Career!")
        print("We would surely Support you in this!")
    else:
        print("Invalid Career!")

def rdmp_fees():
    print("To access the roadmap and further consultation details, we require an additional fee of 99$.")
    paid = input("Have you paid the 99$ for the roadmap? (yes/no): ").capitalize()
    return paid == "Yes"

def deep_research_in_career_path(tp):
    tp = tp.strip().lower() 
    if tp == "medical":
        print("Now, you Need to Follow a Certain Roadmap to Excel in the Medical Field!")
        print()
        rdmp = input("Do you want the Roadmap? (yes/no): ")
        if rdmp.lower() == "yes" and rdmp_fees():
            med_rdmp = [
                "1- Complete 10+2 with PCB (Physics, Chemistry, Biology).", 
                "2- Clear NEET (National Eligibility cum Entrance Test).", 
                "3- Complete MBBS (Bachelor of Medicine, Bachelor of Surgery).", 
                "4- Clear NEXT (National Exit Test) for medical licensing.",
                "5- Pursue MD/MS for specialization (optional).",
                "6- Gain experience through residency/internship.",
                "7- Obtain state/national medical license.",
                "8- Work in hospitals to gain experience and build a network.",
                "9- Pursue further specialization (DM/MCh) if desired.",
                "10- Open or join a clinic/hospital setup."]
            print()
            for step in med_rdmp:   
                print(step)
                print()
            print("""Now, Being into Medical after completing Science Stream in PCB! 
You Must be Clear about your Niche in Medical!
For such Further Consultation & Guidance, reach out to our PCB Stream Manager- Mr Smart, at 123456XXXX
Thank You Very Much!""")
    elif tp == "engineering":
        print("Now, you Need to Follow a Certain Roadmap to Excel in the Engineering Field!")
        print()
        rdmp = input("Do you want the Roadmap? (yes/no): ")
        if rdmp.lower() == "yes" and rdmp_fees():
            eng_rdmp = [
                "1- Complete 10+2 with PCM.",
                "2- Clear JEE (Main & Advanced for IITs).",
                "3- Pursue B.Tech/B.E. in chosen field.",
                "4- Complete internships and projects.",
                "5- Participate in campus placements or pursue M.Tech/MS.",
                "6- Gain job experience and build a network.",
                "7- Consider further specialization (MBA/MS/PhD).",
                "8- Apply for high-paying roles or MNCs."]
            print()
            for step in eng_rdmp:
                print(step)
                print()
            print("""Now, Being into Engineering after completing Science Stream in PCM! 
You Must be Clear about your Niche in Engineering!
For such Further Consultation & Guidance, reach out to our PCM Stream Manager- Mr Happy, at 123456XXXX
Thank You Very Much!""")
    elif tp in ["research & philosophy", "rnp"]:
        print()
        if rdmp_fees():
            print("""Now, Being into Research & Philosophy after completing Science Stream, whether PCM or PCB! 
You Must be Clear about your Niche in Research & Philosophy!
For such Further Consultation & Guidance, reach out to our Research & Philosophy Manager- Ms Good, at 123456XXXX
Thank You Very Much!""")
    elif tp in ["stream neutral", "sn"]:
        if rdmp_fees():
            print("""Now, Being Stream Neutral leads to many Different Career Paths after completing Science Stream, whether PCM or PCB! 
You Must be Clear about your Future & the Career You want to Choose!
For such Further Consultation & Guidance, reach out to our Stream Neutral Manager- Ms Positive, at 123456XXXX
Thank You Very Much!""")
    
    bill()
    
    again = input("Would you like to consult again? (yes/no): ").strip().lower()
    print()
    return again == 'yes'

def bill():
    print("\nHere is your Consultation Bill:")

    consultation_fee = float(input("Enter the Consultation Fee (default is 49$): ") or 49)
    roadmap_fee = float(input("Enter the Roadmap Fee (default is 99$): ") or 99)
    
    total = consultation_fee + roadmap_fee
    
    print(f"Consultation Fees: ${consultation_fee}")
    print(f"Roadmap Fees: ${roadmap_fee}")
    print(f"Total: ${total}")
    print("Thank you for consulting with us!\n")

def final_call():
    welcome_message()
    
    while True:
        ffp = form_fees()
        print()
        if ffp == "Yes":
            hstr = get_high_school_stream()
            print()
            if provide_stream_motivation(hstr):
                print()
                tp = get_career_path()
                print()
                provide_career_advice(tp)
                print()
                if not deep_research_in_career_path(tp):
                    print("Thank you for visiting HSGP Consultations! Good luck with your career!")
                    break
        else:
            again = input("Would you like to consult again? (yes/no): ").strip().lower()
            print()
            if again != 'yes':
                print("Thank you for visiting HSGP Consultations! Good luck with your career!")
                break

final_call()
