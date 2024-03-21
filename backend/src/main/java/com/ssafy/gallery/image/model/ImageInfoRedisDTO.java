package com.ssafy.gallery.image.model;

import jakarta.persistence.Column;
import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;
import org.springframework.data.redis.core.TimeToLive;

import java.time.LocalDateTime;
import java.util.List;
import java.util.concurrent.TimeUnit;

@Getter
@Setter
@NoArgsConstructor
@RedisHash("image")
public class ImageInfoRedisDTO {

    @Id
    private int imageInfoId;

    private String originalImageUrl;
    private String thumbnailImageUrl;
    private String processedImageUrl;

    @TimeToLive(unit = TimeUnit.MILLISECONDS)
    private long expiration;

    public ImageInfoRedisDTO(int imageInfoId) {
        this.imageInfoId = imageInfoId;
    }

    public ImageInfoRedisDTO(ImageInfo image) {
        imageInfoId = image.getImageInfoId();
        originalImageUrl = image.getOriginalImageUrl();
        thumbnailImageUrl = image.getThumbnailImageUrl();
        processedImageUrl = image.getProcessedImageUrl();
        expiration = 60000000;
    }
}
