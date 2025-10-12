# @Course: CS_119 #15492
# @author: Jacob Yeung #900494756
# @Date: 20251009
# @version Lab06 - Ex A (a). Personal Web Page Generator  (15 points)
# */

import html

# Write a program that asks the user for his or her name,
# then asks the user to enter a sentence that describes himself or herself.
# Here is an example of the program’s screen:

#Enter your name: Julie Taylor [Enter]
# Describe yourself: I am a computer science major, a member of the
# Jazz club, and I hope to work as a mobile app developer after I
# graduate. [Enter]

# Once the user has entered the requested input, the program should create an HTML file,
# containing the input, for a simple Web page.
# Here is an example of the HTML content, using the sample input previously shown:

htmlTemplate = """
<html>
\t<head>
\t</head>
\t<body>
\t\t<center>
\t\t\t<h1>{0}</h1>
\t\t</center>
\t\t<hr />
{1}
\t\t<hr />
\t</body>
</html>
""".strip()
maxLenInLine = len("and I hope to work as a mobile app developer after I graduate.")

while True:
    try:
        fullName = input("Enter your name: ").strip()  # "Julie Taylor" => last name: Taylor
        nameList = fullName.split(" ")
        if len(nameList) < 2: raise ValueError("Please enter your full name in format: 'Firstname Lastname'");
        for name in nameList:
            if not name.replace("'",'').replace("-",'').isalpha():
                raise ValueError("Please enter your full name in alpha: 'Firstname Lastname'")

        with open(f"{nameList[len(nameList)-1]}.html", "w") as file:
            print(" Describe yourself: ", end = '')
            selfDescriptionLines = []
            while True:
                line = input()
                if line.strip().endswith('.') or line.strip().endswith('!') or len(line.strip()) == 0:
                    selfDescriptionLines.append(line)
                    break
                selfDescriptionLines.append(line)

            fullName = html.escape(fullName)
            selfDescription = " ".join(selfDescriptionLines).strip().replace('\u2009', '')
            selfDescription = html.escape(selfDescription)
            selfDescriptions = selfDescription.split(",")

            count = 0
            encodedString = ''
            for i in range(len(selfDescriptions)):
                selfDescriptions[i] = selfDescriptions[i].strip()
                if i != len(selfDescriptions) - 1:
                    selfDescriptions[i] += ','

                if count == 0:
                    encodedString += f"\t\t{selfDescriptions[i]}"
                    count = len(selfDescriptions[i])
                elif count + len(selfDescriptions[i]) > maxLenInLine:
                    encodedString += f"\n\t\t{selfDescriptions[i]}"
                    count = len(selfDescriptions[i])
                else:
                    encodedString += ' ' + selfDescriptions[i]
                    count += len(selfDescriptions[i])

            file.write(htmlTemplate.format(fullName, encodedString))
        break
    except ValueError as e:
        print(e)
    except IOError as e:
        print(e)

#https://onlinegdb.com/dJ_XCEaBcM
#Case 1: wall space: 56 & price per Gallon: $3
"""
Please enter the wall space in square feet (sq ft): 56
Please enter the price per Gallon of the wall (price per gallon): $3
--------------------------------------------------------------------

                             Quotation                              
--------------------------------------------------------------------
The wall space in square feet: 56.00sq ft
One gallon of paint: $3.00/gal
The number of gallons of paint required: 0.50gal
The hours of labor required: 4.00hrs
The cost of the paint: $1.50
The labor charges: $140.00
The total cost of the paint job: $141.50
--------------------------------------------------------------------
                          End of Quotation                          


...Program finished with exit code 0
Press ENTER to exit console.
"""
