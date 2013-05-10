package responsibility;
import java.util.ArrayList;
import java.util.List;

public class Macro {
	public List<ISkill> skills=new ArrayList<ISkill>();
	
	public void castSkill(){
		for(int i=0;i<skills.size();i++){
			skills.get(i).castSkill();
		}
	}
	
	public void bindSkill(ISkill skill){
		skills.add(skill);
	}

}
