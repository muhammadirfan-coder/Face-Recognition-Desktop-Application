import tkinter as tk

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root=tk.Tk()
app=FullScreenApp(root)
root.mainloop()