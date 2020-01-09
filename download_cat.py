import urllib.request
import easygui as g

def main():
    msg="Please specify the size of your picture: "
    title="Generate a Meow"

    field=['Width: ', 'Height: ']
    values=[]

    size=width, height=400, 600
    values=g.multenterbox(msg, title, field, size);

    while 1:
        if values == None:
            break
        errmsg=""

        try:
            width=int(values[0].strip())
        except:
            errmsg+="The width must be an integer!"

        try:
            height=int(values[1].strip())
        except:
            errmsg+="The height must be an integer!"

        if errmsg=="":
            break

        values=g.multenterbox(errmsg, title, field, values)


        print("hello")

    url="http://placekitten.com/g/%d/%d" %(width, height)

    response=urllib.request.urlopen(url)
    cat_img=response.read()

    filepath=g.diropenbox("Please select the folder: ")

    if filepath:
            filename='%s/cat_%d_%d.jpg' %(filepath, width, height)
    else:
        filename='cat_%d_%d.jpg' %(width, height)

    with open(filename, 'wb') as f:
        f.write(cat_img)

if __name__ == "__main__":
    main()
