import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
// import com.lmax.disruptor.LifecycleAware;

public class demo {


    static {Runtime.getRuntime().addShutdownHook(new Thread(new Runnable() {

            @Override
            public void run() {
                System.out.println("Exited!");
            }
        }));
    }

    public static void main(String[] args) {
        System.out.println("begin!");
        try{
            Thread.sleep(1000*60);
        } catch (Exception e) {
            e.printStackTrace();
        }
            
            
    }
}