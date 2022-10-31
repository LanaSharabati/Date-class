"""
Write a class named “Date” that 
handles the date, 
containing day, month, and year
***You should be able to instantiate an
 instance using a constructor as follows
d1 = Date(23, 12, 2020)
"""
class Date:
    
    description = " handles the date"
    def __init__(self,dd,mm,yyyy):
        self.__day = dd
        self.__mounth = mm
        self.__year = yyyy
        
        
    def calculate_mounth_days(mounth,year):
        '''
        Parameters
        ----------
        mounth : int
        year : int

        Returns
        -------
        int
            return the days does each month have, 
            taking into account the leap year

        '''
        if mounth == 2:
            if year % 400 == 0 and year % 100 == 0:
                return 29
            elif year % 4 ==0 and year % 100 != 0:
                return 29
            else:
                return 28
        elif mounth ==  4:
            return 30
        elif mounth == 6:
            return 30
        elif mounth == 9 :
            return 30
        elif mounth == 11 :
            return 30
        else:
            return 31
    
    
    def mounth_year_days(mounth,year):
        '''
        Parameters
        ----------
        mounth : int
        year : int
        Returns
        -------
        mounth_days : int
            Calculates the number of days from
            the first month to the current month of the year

        '''
        mounth_days = 0
        for j in range(mounth):
            mounth_days = Date.calculate_mounth_days(mounth,year) + mounth_days
            mounth = mounth -1
        return mounth_days
        
            
    def order(self):
        '''
        Returns
        -------
        string
            returns the order of a specific date in the year

        '''
        p = str(self.__day + Date.mounth_year_days(self.__mounth,self.__year))
        return ( "since " + str(self.__day)+"/"+str(self.__mounth)+" is the "+p+"th day in the year")
           
        
    def __str__(self):  
        return (str(self.__day)+"/"+str(self.__mounth)+"/"+str(self.__year))
        
        
    def __add__(self,other):
       mounth = self.__mounth
       day = self.__day 
       year = self.__year
       for i in range(other):  
           mounth_days = Date.calculate_mounth_days(mounth,year)
           day = day + 1
           if mounth_days < day:
               mounth = mounth +1
               day = 1
               if mounth == 13:
                    mounth = 1
                    year = self.__year + 1
       return Date(day,mounth,year)
       
   
    def __sub__(self,other):
        day = [self.__day ,other.__day]
        year = [self.__year , other.__year]
        mounth = [self.__mounth , other.__mounth]

        for i in range(2):
            year[i] = year[i]*365
            mounth_days = Date.mounth_year_days(mounth[i],year[i])
            day[i] = year[i] - mounth_days - day[i]
        return str(abs(day[1]-day[0]))+" day "
    
    
    def __lt__(self,other):
        if (self.__year < other.__year):
            return True
        elif(self.__year > other.__year):
            return False
        elif (self.__mounth < other.__mounth):
            return True
        elif (self.__mounth > other.__mounth):
            return False
        elif (self.__day < other.__day):
            return True
        elif (self.__day > other.__day):
            return False
    
        
    def __le__(self,other):
        if (self.__year < other.__year):
            return True
        elif(self.__year > other.__year):
            return False
        elif (self.__mounth < other.__mounth):
            return True
        elif (self.__mounth > other.__mounth):
            return False
        elif (self.__day <= other.__day):
            return True
        elif (self.__day >= other.__day):
            return False
        

    def set_day(self, dd):
        self.__day = dd
        
        
    def get_day(self):
        return self.__day
    
    
    def set_mounth(self, mm):
        self.__mounth = mm
        
        
    def get_mounth(self):
        return self.__mounth
    
    
    def set_year(self, yyyy):
        self.__year = yyyy
        
        
    def get_year(self):
        return self.__year
    
    
    day= property(get_day,set_day)
    year= property(get_year,set_year)
    mounth= property(get_mounth,set_mounth)
    
        

d1 =Date(1, 11, 2020)
d3 = Date(1,12,2022)
d4 =Date(1, 11, 2020)

print(d1.order())
print("d1 = ",d1)
d2 = d1 + 22
print("d2 = ",d2)
number_of_days = d2 - d1 
print("number_of_days",number_of_days)

if d1 > d2:
    print("yes d1 greater than  d2")
else:
    print("no d1 Smaller than d2")


    

        
