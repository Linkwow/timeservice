FROM eclipse-temurin:21-alpine AS builder

WORKDIR /build
RUN chmod +x mvnw
COPY .mvn .mvn
COPY pom.xml mvnw ./
RUN ./mvnw dependency:resolve

COPY src src
RUN ./mvnw clean install

FROM eclipse-temurin:21-alpine AS extractor

WORKDIR /extract
COPY --from=builder /build/target/*.jar app.jar

RUN java -Djarmode=tools -jar app.jar extract --layers --destination extracted

FROM eclipse-temurin:21-alpine AS application

WORKDIR /app
COPY --from=extractor /extract/extracted/dependencies/ ./
COPY --from=extractor /extract/extracted/spring-boot-loader/ ./
COPY --from=extractor /extract/extracted/snapshot-dependencies/ ./
COPY --from=extractor /extract/extracted/application/ ./

ENTRYPOINT ["java", "-jar", "app.jar"]