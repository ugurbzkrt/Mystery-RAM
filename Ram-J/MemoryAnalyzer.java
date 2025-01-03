import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;

public class MemoryAnalyzer {
    public static void main(String[] args) {
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();

        MemoryUsage heapUsage = memoryBean.getHeapMemoryUsage();
        System.out.println("Heap Memory:");
        System.out.println("  Used: " + heapUsage.getUsed());
        System.out.println("  Max: " + heapUsage.getMax());
        System.out.println("  Committed: " + heapUsage.getCommitted());

        MemoryUsage nonHeapUsage = memoryBean.getNonHeapMemoryUsage();
        System.out.println("\nNon-Heap Memory:");
        System.out.println("  Used: " + nonHeapUsage.getUsed());
        System.out.println("  Max: " + nonHeapUsage.getMax());
        System.out.println("  Committed: " + nonHeapUsage.getCommitted());
    }
}
