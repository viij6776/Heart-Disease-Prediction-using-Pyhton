from appJar import gui
from numpy import genfromtxt
import numpy as np
from sklearn.naive_bayes import GaussianNB
def CalculateDisease(button):
    if button=="Reset":
        app.setEntry("A1","")
        app.setEntry("A2","")
        app.setEntry("A3","")
        app.setEntry("A4","")
        app.setEntry("A5","")
        app.setEntry("A6","")
        app.setEntry("A7","")
        app.setEntry("A8","")
        app.setEntry("A9","")
        app.setEntry("A10","")
        app.setEntry("A11","")
        app.setEntry("A12","")
        app.setEntry("A13","")
        app.setEntry("A14","")
    elif button=="Close":
        app.stop()
    else:
        dataset = genfromtxt('cleveland_data.csv',dtype = float, delimiter=',')
        X = dataset[:,0:13] #Feature Set
        y = dataset[:,13]   #Label Set
        a=int(app.getEntry("A1"))
        b=int(app.getEntry("A2"))
        c=int(app.getEntry("A3"))
        d=int(app.getEntry("A4"))
        e=int(app.getEntry("A5"))
        f=int(app.getEntry("A6"))
        g=int(app.getEntry("A7"))
        h=int(app.getEntry("A8"))
        i=int(app.getEntry("A9"))
        j=float(app.getEntry("A10"))
        k=int(app.getEntry("A11"))
        l=int(app.getEntry("A12"))
        m=int(app.getEntry("A13"))
        #z=z.reshape(14, 1)
       # X=[[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
        #y = np.array([1, 1, 1, 2, 2, 2])
        model = GaussianNB()
        model.fit(X, y)
        predicted= model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m]])
        #predicted= model.predict(z)
        print(predicted)
        if predicted == 0:
           app.showSubWindow("Result Level 0")
			
        elif predicted == 1:
            app.showSubWindow("Result Level 1")
		
        elif predicted == 2:
            app.showSubWindow("Result Level 2")
            
        elif predicted == 3:
            app.showSubWindow("Result Level 3")
		
        elif predicted == 4:
            app.showSubWindow("Result Level 4")
            
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if usr=="Admin" and pwd=="Admin":
            app.hide()
            app.showSubWindow("AfterLogin")
        else:
            app.showSubWindow("Error Message")
app = gui("MainWindow","500x265")
##
app.addLabel("Welcome To Heart Disease Prediction")
app.setBg("Blue")
app.setFg("orange")
app.startLabelFrame("Login Details")
app.setBg("orange")
app.setFg("Black")
app.setFont(18)
app.setSticky("ew")
app.setFont(12)
app.addLabel("l0", "Username:", 0, 0)
app.addEntry("Username", 0, 1)
app.addLabel("l01", "Password:", 1, 0)
app.addSecretEntry("Password", 1, 1)
app.addButtons(["Submit", "Cancel"], press, 2, 0, 2)
app.stopLabelFrame()
##

# create a mesh to plot in
#x_min, x_max = X_new[:, 0].min() - 1, X_new[:, 0].max() + 1
#y_min, y_max = X_new[:, 1].min() - 1, X_new[:, 1].max() + 1
#xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
#                    np.arange(y_min, y_max, 0.02))

# title for the plots
#titles = 'SVC (RBF kernel)- Plotting highest varied 2 PCA values'


# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
#plt.subplot(2, 2, i + 1)
#plt.subplots_adjust(wspace=0.4, hspace=0.4)
#Z = modelSVM2.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
#Z = Z.reshape(xx.shape)
#plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
# Plot also the training points
#plt.scatter(X_new[:, 0], X_new[:, 1], c=y, cmap=plt.cm.Paired)
#plt.xlabel('PCA 1')
#plt.ylabel('PCA 2')
#plt.xlim(xx.min(), xx.max())
#plt.ylim(yy.min(), yy.max())
#plt.xticks(())
#plt.yticks(())
#plt.title(titles)
#plt.show()


##
app.startSubWindow("AfterLogin", modal=True)
app.addLabel("s1","Welcome To Heart Disease Prediction")
app.setFg("ornage")
app.setBg("Blue")
app.setLabelBg("s1", "blue")
app.startLabelFrame("Patients Test Details")
app.setFg("Black")
app.setBg("orange")#d2f7ee
app.addLabel("l1", "1. Age:", 0, 0)
app.addEntry("A1", 0, 1)
app.addLabel("l2", "2. Sex:\t1-male\n\t0-female", 1, 0)
app.addEntry("A2", 1, 1)
app.addLabel("l3", "3. Chest Pain Type:\n\t1-Typical\n\t2- Atypical\n\t3-Non-anginal\n\t4-Asymptomatic:", 2, 0)#
app.addEntry("A3", 2, 1)
#app.addLabel("lc", "1-typical \n 2- atypical\n 3-non-anginal\n4-asymptomatic:", 2, 0)
app.addLabel("l4", "4. Blood Pressure(mmHg)", 3, 0)
app.addEntry("A4", 3, 1)
app.addLabel("l5", "5. Cholestoral(mg/dl)", 4, 0)
app.addEntry("A5", 4, 1)
app.addLabel("l6", "6. Fasting Blood Sugar:\n\t(>120 mg/dl)(1 = true; 0 = false))", 5, 0)
app.addEntry("A6", 5, 1)
app.addLabel("l7", "7. Resting ECG Results:\n\t0: normal\n\t1: having ST-T wave abnormality\n\t2: showing probable/definite left ventricular hypertrophy", 6, 0)
app.addEntry("A7", 6, 1)
app.addLabel("l8", "8. Maximum Heart Rate Achieved:", 7, 0)
app.addEntry("A8", 7, 1)
app.addLabel("l9", "9. Exercise induced angina:\n\t1 = yes\n\t0 = no", 8, 0)
app.addEntry("A9", 8, 1)
app.addLabel("l10", "10. ST depression induced by exercise relative to rest:", 9, 0)
app.addEntry("A10", 9, 1)
app.addLabel("l11", "11. Slope:\t1: upsloping\n\t2: flat\n\t3: downsloping", 10, 0)
app.addEntry("A11", 10, 1)
app.addLabel("l12", "12. Number of major vessels (0-3) colored by flourosopy", 11, 0)
app.addEntry("A12", 11, 1)
app.addLabel("l13", "13. Thal:\n\t3 = normal;\n\t6 = fixed defect;\n\t7 = reversable defect", 12, 0)
app.addEntry("A13", 12, 1)
#pp.addLabel("l14", "14. Name", 13, 0)
#pp.addEntry("A14", 13, 1)
app.addButtons(["Calculate", "Reset","Close"], CalculateDisease, 14, 1)
app.stopLabelFrame()
app.stopSubWindow()
##
app.startSubWindow("Error Message", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("Wrong username or Password")
app.stopSubWindow()
##
app.startSubWindow("Output Message", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("Your Disease Name=")
app.stopSubWindow()
##
app.startSubWindow("Result Level 0", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("GREAT...YOU ARE STRONG AND FIT...!!!")
app.stopSubWindow()
##
app.startSubWindow("Result Level 1", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("PRESENCE OF DISEASE : LESS THAN 25%(NEGLIGIBLE)")
app.stopSubWindow()
##
app.startSubWindow("Result Level 2", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("PRESENCE OF DISEASE: LESS THAN 50%(NEED TO BE CAREFULL)")
app.stopSubWindow()
##
app.startSubWindow("Result Level 3", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("DISEASE...!!! NEEDS FOR TREATMENT..STEPPING TOWARDS HIGH RISK")
app.stopSubWindow()
##
app.startSubWindow("Result Level 4", modal=True)
app.setBg("Black")
app.setFg("White")
app.addLabel("BE CAREFUL...HIGH RISK!!!")
app.stopSubWindow()
##
            
app.go()

##====================ANOTHER COMBINATION========
#class simpleapp_wx(wx.Frame):
#    def __init__(self,parent,id,title):
# #      wx.Frame.__init__(self,parent,id,title)
#    #    self.parent = parent
#       self.initialize()
#
#   def initialize(self):
#   #     sizer = wx.GridBagSizer()
# #      self.entry = wx.TextCtrl(self,-1,value=u"Enter text here.")
#    #    sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
#
#      button = wx.Button(self,-1,label="Click me !")
#    #    sizer.Add(button, (0,1))
#
#      self.label = wx.StaticText(self,-1,label=u'Hello !')
#    #    self.label.SetBackgroundColour(wx.BLUE)
#     #  self.label.SetForegroundColour(wx.WHITE)
#        #sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )
#
#  #      sizer.AddGrowableCol(0)
#    ##     
#     #   self.SetSizerAndFit(sizer)
#       # self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
#        self.Show(True)

#if __name__ == "__main__":
#    app = wx.App()
#    frame = simpleapp_wx(None,-1,'my application')
#    app.MainLoop()

#=================



