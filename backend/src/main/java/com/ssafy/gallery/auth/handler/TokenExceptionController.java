package com.ssafy.gallery.auth.handler;

import com.ssafy.gallery.auth.exception.AuthExceptionEnum;
import com.ssafy.gallery.common.exception.ApiExceptionFactory;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("/api/v1/exception")
public class TokenExceptionController {

    @GetMapping("/entrypoint")
    public void entryPoint() {
        log.error("로그인이 필요합니다");
        throw ApiExceptionFactory.fromExceptionEnum(AuthExceptionEnum.NO_LOGIN);
    }

    @GetMapping("/accessDenied")
    public void denied() {
        log.error("권한이 없습니다");
        throw ApiExceptionFactory.fromExceptionEnum(AuthExceptionEnum.NO_ADMIN);
    }
}