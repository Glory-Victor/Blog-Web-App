class MainControl:
    def __init__(self,opt):
        self.opt = opt


    def selection(self):
        if self.opt == 1:
            print ("1. Create a new blog post:")
            print (obj.blogpost())
        elif self.opt == 2:
            print ("2. List all the Title:")
            print (obj.title())
            return BlogPost(opt)
        else:
            print ("3. Retrieve the Content based on Title:")
            print (obj.content())
            return BlogPost(opt)

class BlogPost(MainControl):
    def __init__(self,opt):
        MainControl.__init__(self,opt)

    #for updating the blog data in dictionary
    def blogpost(self):
        a = raw_input("Enter a Title")
        b = raw_input("Enter the content")
        blog[a]=b

    #for listing out the title
    def title(self):
        newlist = list()
        for i in blog.keys():
            newlist.append(i)
        print (newlist)

    #for retrieving the content
    def content(self):
        con = raw_input("Enter a Title")
        for key in blog:
            if key == con:
                print (blog[key])

blog = {}

while True:
    opt = int(input("Select an Option \n 1. Create a new blog post \n 2. List all the title \n 3. Retrieve the content by selecting the title \n"))

    obj = BlogPost(opt)

    obj.selection()
