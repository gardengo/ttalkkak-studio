package com.ssafy.gallery.common.exception;

public class ApiExceptionFactory {

    public static ApiException fromExceptionEnum(ExceptionEnum exceptionEnum) {
        System.out.println(exceptionEnum.getStatus());
        return new ApiException(
                exceptionEnum.getStatus(),
                exceptionEnum.getCode(),
                exceptionEnum.getMessage()
        );
    }

}