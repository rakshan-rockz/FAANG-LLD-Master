# My Concurrency Primitives Sheet

Written by you after each Phase 6–7 session; Claude verifies. The *classic bug* column is the one interviewers probe.

| Primitive (C++ · Java) | What it guarantees | Typical use | The classic bug (and its interleaving) | How I test it | Cost / when NOT |
|---|---|---|---|---|---|
| std::thread / std::jthread (+ stop_token) · Java Thread | | | | | |
| std::mutex + lock_guard / unique_lock / scoped_lock · synchronized / ReentrantLock | | | | | |
| std::condition_variable (predicate wait) · wait/notify, Condition | | | | | |
| std::atomic (+ CAS loop) · AtomicInteger / LongAdder / volatile | | | | | |
| Memory orders: seq_cst / acquire / release / relaxed · JMM happens-before | | | | | |
| std::shared_mutex · ReentrantReadWriteLock / StampedLock | | | | | |
| std::counting_semaphore / binary_semaphore · Semaphore | | | | | |
| std::latch · CountDownLatch | | | | | |
| std::barrier · CyclicBarrier / Phaser | | | | | |
| std::promise / future / packaged_task / async · Future / CompletableFuture | | | | | |
| std::call_once / magic statics · holder idiom / enum singleton | | | | | |
| Bounded blocking queue · ArrayBlockingQueue / LinkedBlockingQueue | | | | | |
| Thread pool · ExecutorService / ThreadPoolExecutor | | | | | |
| Work-stealing pool · ForkJoinPool | | | | | |
| Striped / concurrent map · ConcurrentHashMap | | | | | |
| Token bucket rate limiter · Guava RateLimiter | | | | | |
| Delayed-task scheduler · ScheduledThreadPoolExecutor / DelayQueue | | | | | |

## Hazards → strategies

| Hazard | Example | Prevention I'd use | Why not the alternatives |
|---|---|---|---|
| Lost update | | | |
| Check-then-act | | | |
| Compound invariant across fields | | | |
| Deadlock | | | |
| Livelock | | | |
| Starvation | | | |
| Lost wakeup / spurious wakeup | | | |
| Double booking | | | |
| Double spend | | | |
| Write skew | | | |
| Duplicate processing on retry | | | |
