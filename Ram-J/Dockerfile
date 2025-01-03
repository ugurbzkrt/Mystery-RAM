FROM openjdk:11
COPY MemoryAnalyzer.java /app/MemoryAnalyzer.java
WORKDIR /app

RUN javac MemoryAnalyzer.java

CMD ["java", "MemoryAnalyzer"]
