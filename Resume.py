import streamlit as st

def main():
    st.set_page_config(page_title="My Resume", layout="wide")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me","Education", "Work Experiences", "Organization Experiences", "Projects", "Achievements"])

    if page == "About Me":
        about_me()
    elif page == "Education":
        education()
    elif page == "Work Experiences":
        work_experiences()
    elif page == "Organization Experiences":
        organization_experiences()
    elif page == "Projects":
        projects()
    elif page == "Achievements":
        achievements()

def about_me():
    st.title("Online Resume Muhammad Aqshal Julian")
    st.markdown("## About Me")
    st.write("Hello! I'm Muhammad Aqshal Julian, i’m a fresh graduate who have a Diploma Degree of Computer Software Engineering from Universitas Indonesia (CCIT FTUI) and took a Bachelor Degree of Computer Science and Engineering from STTI NIIT, and im looking for job opportunities that can be helpful right now and in the future. I’m a great team player, good at communication, eager to learn, and have a good strategic thinking. Other than academics, i also participated in organizational activity.")
    st.write("Reach Me Out via Email : aqshaljulian123@gmail.com")
    st.write("Reach Me Out via Linkedin : https://www.linkedin.com/in/muhammad-aqshal-julian/")
    st.write("Feel free to explore my resume and learn more about my background, experiences, and projects.")

    col1, col2, col3, col4, col5, col6= st.columns(6)

    with col1:
        st.image("WhatsApp Imag-12-26 at 2.02.30 PM.jpeg", use_container_width=True)
    with col2:
        st.image("WhatsApp Image 2024-12-26 at 2.02.31 PM-3.jpeg", use_container_width=True)
    with col3:
        st.image("WhatsApp Image 2024-12-26 at 2.02.31 PM.jpeg", use_container_width=True)
    with col4:
        st.image("WhatsApp Image 2024-12-26 at 2.02.32 PM.jpeg", use_container_width=True)
    with col5:
        st.image("WhatsApp Image 2024-12-26 at 2.02.32 PM-2.jpeg", use_container_width=True)
    with col6:
        st.image("BFI .jpeg", use_container_width=True)

def work_experiences():
    st.title("Work Experiences")
    st.write("### PT BFI Finance Indonesia")
    st.write("**Position:** Data Innovation Internship")
    st.write("**Duration:** May 2024 - Present")
    st.write("- OCR customer's personal identity such as ID Card, NPWP, STNK, BPKB, etc using PaddlePaddle.")
    st.write("- Help to train machine learning to identify words, numbers, and pictures to be more accurate.")
    st.write("- Adding subtitles to Speech-to-Text conversation between customer service and customers.")
    st.write("- Upload daily task to Alibaba Cloud.")
    st.write("- Create an NLP Project by collecting remarks from agent collectors.")

    st.write("### PT Sinarmas Distribusi Nusantara")
    st.write("**Position:** IT Department Internship")
    st.write("**Duration:** May 2022 - Aug 2022")
    st.write("- Receiving, Recap to Database and Sending IT Units (Laptops, Printers, PCs, etc.) ")
    st.write("- Helping to deliver IT Units to Branch Office.")
    st.write("- Checking daily email.")
    st.write("- Recap every IT Units purchase to Database (with approval from HR GA complete with purchase receipt, serial number, etc.)")
    st.write("- Prepare Laptop or PC before sending to Branch Office or personal user in Head Office.")

    st.write("### PT Leon Boga Sentosa")
    st.write("**Position:** IT Support Internship")
    st.write("**Duration:** Jan 2022 - Apr 2022")
    st.write("- Managing the recap and storing employees data into company's server.")
    st.write("- Helping to troubleshoot some issues on software and hardware in other employees gadgets (laptops, applications, PCs, printers, etc).")
    st.write("- Make a revision to redactional article and products posted in official website.")
    st.write("- Post products to official online store in Tiktok Shop and Shopee.")

def education():
    st.title("Education")
    st.write("### Sekolah Tinggi Teknologi Informasi NIIT")
    st.write("**Degree:** Bachelor of Science in Computer Science and Engineering")
    st.write("**Graduation Year:** 2024")
    st.write("**Grade:** 3.32/4.00")
    

    st.write("### Universitas Indonesia")
    st.write("**Degree:** Diploma of Computer Software Engineering")
    st.write("**Graduation Year:** 2023")
    st.write("**Grade:** 3.08/4.00")
    col1, col2 = st.columns(2)
    with col1:
        st.image("Lulus FTUI 1.jpeg", caption="Universitas Indonesia", width=200)
    with col2:
        st.image("Lulus FTUI 2.jpeg", caption="Universitas Indonesia", width=200)

    
    st.write("### SMA Negeri 12 Tangerang Selatan")
    st.write("**Graduation Year:** 2019")
    st.write("**Major:** MIPA")
    st.write("**Average Graduation Grade:** 83.00")


def organization_experiences():
    st.title("Organization Experiences")
    st.write("### Himpunan Mahasiswa Islam Komisariat FEB UI")
    st.write("**Organization:** Himpunan Mahasiswa Islam")
    st.write("**Duration:** 2020 - 2021")
    col1, col2 = st.columns(2)
    with col1:
        st.image("Sertifikat HMI.jpeg", caption="Sertifikat HMI UI", width=200)

    st.write("### OSIS")
    st.write("**Organization:** OSIS SMA Negeri 12 Tangerang Selatan")
    st.write("**Duration:** 2017 - 2018")
    

def projects():
    st.title("Projects")
    st.write("### Kopi Ambyar User Interface (Universitas Indonesia)")
    st.write("- Built a fully functional website user interface platform with Products Listing, Home Page, Opening Hours and About Us.")
    st.write("- Tech Stack: HTML, CSS")

    st.write("### Reservation for Fatamorgana Coffee House User Interface (Sekolah Tinggi Teknologi Informasi NIIT)")
    st.write("- Developed a User Interface Website with functional Reservation System, Homepage, Products Listing, Location, and Explore Function.")
    st.write("- Tech Stack: C++, MySQL, CSS")

    st.write("### NLP Project User Interface for Visualization Deployment (PT BFI Finance Indonesia)")
    st.write("- Developed a User Interface for visualize NLP results by collecting Agent Collector Remarks.")
    st.write("- Developed a User Interface for visualize data reports, and graphics.")
    st.write("- Achieved 85% accuracy using Random Forest, 83% accuracy using SVM, and 75% accuracy using Naive Bayes.")
    st.write("- Tech Stack: Python, Scikit-learn, Pandas")

def achievements():
    st.title("Achievements and Certifications")
    st.write("### CCIT - NIIT Certificate of Professional Program")
    st.write("- Description: Completed a 2 year Diploma Study in CCIT FTUI Universitas Indonesia with Good grade.")
    st.write("- Issued Year: 2024")
    col1, col2 = st.columns(2)
    with col1:
        st.image("Sertifikat NIIT.jpeg", caption="CCIT - NIIT Certication of Professional Program", width=200)

    st.write("### CCNA: Switching, Routing and Wireless Essentials")
    st.write("- Description: Successfully completed module taken in Cisco Certification Training in Sekolah Tinggi Teknologi Informasi NIIT.")
    st.write("- Issued Year: 2024")
    st.write("- Credential: https://www.credly.com/badges/016713d5-a548-4988-8aa1-b47a3c9dcc3f/linked_in_profile")

    st.write("### CCNA: Enterprise Networking, Security, and Automation")
    st.write("- Description: Successfully completed module taken in Cisco Certification Training in Sekolah Tinggi Teknologi Informasi NIIT.")
    st.write("- Issued Year: 2023")
    st.write("- Credential: https://www.credly.com/badges/f0f25814-4691-473a-a601-c232724ee59a/linked_in_profile")

    st.write("### CCNA: Introduction to Networks")
    st.write("- Description: Successfully completed module taken in Cisco Certification Training in Sekolah Tinggi Teknologi Informasi NIIT.")
    st.write("- Issued Year: 2023")
    st.write("- Credential: https://www.credly.com/badges/2938b7d6-0df0-4edf-b9c6-1713f3435b1f/linked_in_profile")

if __name__ == "__main__":
    main()
