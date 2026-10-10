package dev.astropunk.handbook;

import guideme.Guide;
import guideme.GuideBuilder;
import guideme.compiler.TagCompiler;
import net.minecraft.resources.ResourceLocation;

/** Public GuideME builder registration. A same-id JSON guide overrides this guide. */
public final class HandbookQueryGuide {
    private HandbookQueryGuide() {}
    public static GuideBuilder withQueries(GuideBuilder builder, EmiSearchTagCompiler compiler) {
        return builder.extension(TagCompiler.EXTENSION_POINT, compiler);
    }
    public static Guide register() {
        return withQueries(Guide.builder(ResourceLocation.fromNamespaceAndPath("astropunk", "handbook"))
                        .itemSettings(new guideme.GuideItemSettings(
                                java.util.Optional.of(net.minecraft.network.chat.Component.literal("Astropunk Handbook")),
                                java.util.List.of(), java.util.Optional.empty())),
                new EmiSearchTagCompiler()).build();
    }
}
