dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")


import re
def phone(strng, num):
    strings = strng.split("\n")
    name = []
    street = ''
    number = ''
    st   = []
    for element in strings:
        for i in element.split():
            searching = re.search(r"\d{1,2}-\d{3}-\d{3}-\d{3,4}",i)
            if searching and searching.group() == num:
                st.append(element)
    if len(st) > 1 :
        return f"Error => Too many people: {num}"        
    if st == [] : return f"Error => Not found: {num}"
    
    strings = st[0].strip().split()
    print(strings)
    temp = []
    for elem in strings:
        if "<" in elem or ">" in elem: 
            name.append(elem.replace('<','').replace('>',''))
        elif len([i for i in elem if i.isdigit()]) > 10:
            number += elem.replace(',',' ').replace(':','').replace('/','').replace('?','').replace('!','').replace('*','').replace('$','').replace('/','').replace('+','').replace(';','').replace('_','')
        else:
            print(temp)
            temp.append(elem.replace(',',' ').replace('_',' ').replace('/',' ').replace('?',' ').replace('!',' ').replace('*',' ').replace('$',' ').replace('/',' ').replace('+',' ').replace(';',' ').replace('_',' ').strip())
    print(number,' '.join(name),' '.join(temp))
    print(f"Phone => {number}, Name => {' '.join(name)}, Address => {' '.join(temp)}")
    return f"Phone => {number}, Name => {' '.join(name)}, Address => {' '.join(temp)}"
#     print(st[0].strip())
#     nums = re.search(r"\+\d{1,2}(-\d{3}){2}-\d{1,2}",strings)
#     if nums :
#         print(nums.group())
#     print(type(strings))
                
                
                
                
                
#                 print(len(searching.group()))
#                 print((searching.group()))
#             else:
#                 return f"Error => Not found: {num}"
        
        
        
        
        
#         if 11 == len([i for i in element if i.isdigit()]):
#             print(element)
#         if "Anastasia" in element:


#After deleteing the print
# After deleteing the print
import re
def phone(strng, num):
    strings = strng.split("\n")
    st   = []
    for element in strings:
        for i in element.split():
            searching = re.search(r"\d{1,2}-\d{3}-\d{3}-\d{3,4}",i)
            if searching and searching.group() == num:
                st.append(element)
    if len(st) > 1 :
        return f"Error => Too many people: {num}"        
    if st == [] : return f"Error => Not found: {num}"    
    strings = st[0].strip().split()
    name = []
    temp = []
    number = ''
    for elem in strings:
        if "<" in elem or ">" in elem: 
            name.append(elem.replace('<','').replace('>',''))
        elif len([i for i in elem if i.isdigit()]) > 10:
            number += elem.replace(',',' ').replace(':','').replace('/','').replace('?','').replace('!','').replace('*','').replace('$','').replace('/','').replace('+','').replace(';','').replace('_','')
        else:
            temp.append(elem.replace(',',' ').replace('_',' ').replace('/',' ').replace('?',' ').replace('!',' ').replace('*',' ').replace('$',' ').replace('/',' ').replace('+',' ').replace(';',' ').replace('_',' ').strip())
    return f"Phone => {number}, Name => {' '.join(name)}, Address => {' '.join(temp)}"






print(phone(dr, "48-421-674-8974"), "\nPhone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
print(phone(dr, "1-921-512-2222"), "\nPhone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
print(phone(dr, "1-908-512-2222"), "\nPhone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
print(phone(dr, "1-541-754-3010"), "\nPhone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
print(phone(dr, "1-121-504-8974"), "\nPhone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
print(phone(dr, "1-498-512-2222"), "\nPhone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
print(phone(dr, "1-098-512-2222"), "\nError => Too many people: 1-098-512-2222")
print(phone(dr, "5-555-555-5555"), "\nError => Not found: 5-555-555-5555")