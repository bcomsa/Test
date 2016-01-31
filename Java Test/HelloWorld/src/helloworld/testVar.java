package helloworld;
import java.util.regex.*;
import java.lang.*;
public class testVar {
	public static void	 main(String[] args){
		String temp = "asdasd";
		Pattern r = Pattern.compile("^[a-zA-Z][a-zA-Z0-9]*?$");
		Matcher variableName = r.matcher(temp);
		if (!variableName.find() || isJavaKeyword(temp)){
			System.out.println("khong hop le");
		}
		else
			System.out.println("hop le");
	}
	static final String keywords[] = {
        "abstract",  "assert",       "boolean",    "break",      "byte",      "case",
        "catch",     "char",         "class",      "const",     "continue",
        "default",   "do",           "double",     "else",      "extends",
        "false",     "final",        "finally",    "float",     "for",
        "goto",      "if",           "implements", "import",    "instanceof",
        "int",       "interface",    "long",       "native",    "new",
        "null",      "package",      "private",    "protected", "public",
        "return",    "short",        "static",     "strictfp",  "super",
        "switch",    "synchronized", "this",       "throw",     "throws",
        "transient", "true",         "try",        "void",      "volatile",
        "while"
    };


	public static boolean isJavaKeyword(String keyword) {
       for(int i = 0; i < keywords.length; ++i){
    	   if (keyword.equals(keywords[i])){
    		   return true;
    	}
       }
       return false;
   public static boolean isValidJavaIdentifier(String s) {
    	    if (s.isEmpty()) {
    	        return false;
    	    }
    	    if (!Character.isJavaIdentifierStart(s.charAt(0))) {
    	        return false;
    	    }
    	    for (int i = 1; i < s.length(); i++) {
    	        if (!Character.isJavaIdentifierPart(s.charAt(i))) {
    	            return false;
    	        }
    	    }
    	    return true;
    	}
} 
}
