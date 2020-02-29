import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
// import com.lmax.disruptor.LifecycleAware;
//要注意让java进程的pid为1，不然docker stop信号接收不到
public class demo {

    public static void main(String[] args) {

        Runtime.getRuntime().addShutdownHook(new Thread(new Runnable() {

            @Override
            public void run() {
                System.out.println("Exited!");
            }
        }));

        System.out.println("begin!");
        try{
            Thread.sleep(1000*60);
        } catch (Exception e) {
            e.printStackTrace();
        }
            
            
    }
}
