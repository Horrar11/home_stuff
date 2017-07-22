public class Contact{
    private String name;
    private int countryCode, areaCode, simCode;
    
    public Contact(String name, int country, int area, int sim){
	this.name = name;
	areaCode = area;
	simCode = sim;
	System.out.println("New Entry:\n"+name+" - +"+country+"("+area+")"+sim);
    }



    
}
