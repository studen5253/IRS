from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class catagoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Record System | Developed by Deep OP")
        self.root.config(bg="white")
        self.root.focus_force()
        #===Variables===
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #===title===
        lbl_title=Label(self.root,text="Manage Product Catagory",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10, pady=20)
        
        lbl_name=Label(self.root,text="Enter Catagory Name",font=("goudy old style",30),bg="white",).place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightblue",).place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)


        #===Catagory Details===

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.catagory_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.catagory_table.xview)
        scrolly.config(command=self.catagory_table.yview)
        self.catagory_table.heading("cid",text="C ID")
        self.catagory_table.heading("name",text="NAME")
        self.catagory_table["show"]="headings"
        self.catagory_table.column("cid",width=90)
        self.catagory_table.column("name",width=90)
        self.catagory_table.pack(fill=BOTH,expand=1)
        # self.catagory_table.bind("<ButtonRelease-1>",self.get_data)

        #===IMAGES===
        self.im1=Image.open("IRS\images\images\cat.jpg")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("IRS\images\images\category.jpg")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("ERROR","Category name should be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","CATEGORY ALREADY ASSIGNED, try different", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(
                                                self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Catagory added successfully",parent=self.root)
                    self.show()   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.catagory_table.delete(*self.catagory_table.get_children())
            for row in rows:
                self.catagory_table.insert('',END,values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=catagoryClass(root)
    root.mainloop()