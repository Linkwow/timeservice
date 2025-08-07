package com.demo.project.timeservice;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
class TimeServiceApplicationTests {

    @Test
    void shouldGetGlobalEnvVar() {
        var envVar = System.getenv("MY_GLOBAL_ENV_VAR");
        assertThat(envVar).isEqualTo("step");
    }

}
