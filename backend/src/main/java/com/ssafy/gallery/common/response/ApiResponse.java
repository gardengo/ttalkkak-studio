
package com.ssafy.gallery.common.response;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * api 요청 응답 클래스
 * @param <T>
 */
@Data
@NoArgsConstructor
public class ApiResponse<T> {
    private String status;
    private String message;
    private T data;

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>("success", null, data);
    }

    public static ApiResponse<?> error(String message) {
        return new ApiResponse<>("fail", message, null);
    }

    @Builder
    public ApiResponse(String status, String message, T data) {
        this.status = status;
        this.message = message;
        this.data = data;
    }
}
